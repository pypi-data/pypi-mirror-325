import { i as pe, a as U, r as _e, g as he, w as S } from "./Index-CyeKoFiT.js";
const T = window.ms_globals.React, fe = window.ms_globals.React.forwardRef, K = window.ms_globals.React.useRef, R = window.ms_globals.React.useState, O = window.ms_globals.React.useEffect, me = window.ms_globals.React.useCallback, B = window.ms_globals.ReactDOM.createPortal, ge = window.ms_globals.internalContext.useContextPropsContext, J = window.ms_globals.internalContext.ContextPropsProvider, xe = window.ms_globals.antd.theme, we = window.ms_globals.antd.Spin, be = window.ms_globals.antd.Alert;
var ye = /\s/;
function Ee(e) {
  for (var t = e.length; t-- && ye.test(e.charAt(t)); )
    ;
  return t;
}
var Ce = /^\s+/;
function ve(e) {
  return e && e.slice(0, Ee(e) + 1).replace(Ce, "");
}
var X = NaN, Ie = /^[-+]0x[0-9a-f]+$/i, Te = /^0b[01]+$/i, ke = /^0o[0-7]+$/i, Re = parseInt;
function Y(e) {
  if (typeof e == "number")
    return e;
  if (pe(e))
    return X;
  if (U(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = U(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = ve(e);
  var o = Te.test(e);
  return o || ke.test(e) ? Re(e.slice(2), o ? 2 : 8) : Ie.test(e) ? X : +e;
}
var F = function() {
  return _e.Date.now();
}, Oe = "Expected a function", Pe = Math.max, Le = Math.min;
function Se(e, t, o) {
  var s, i, n, r, l, d, h = 0, g = !1, c = !1, _ = !0;
  if (typeof e != "function")
    throw new TypeError(Oe);
  t = Y(t) || 0, U(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Pe(Y(o.maxWait) || 0, t) : n, _ = "trailing" in o ? !!o.trailing : _);
  function f(u) {
    var E = s, I = i;
    return s = i = void 0, h = u, r = e.apply(I, E), r;
  }
  function v(u) {
    return h = u, l = setTimeout(x, t), g ? f(u) : r;
  }
  function m(u) {
    var E = u - d, I = u - h, L = t - E;
    return c ? Le(L, n - I) : L;
  }
  function p(u) {
    var E = u - d, I = u - h;
    return d === void 0 || E >= t || E < 0 || c && I >= n;
  }
  function x() {
    var u = F();
    if (p(u))
      return w(u);
    l = setTimeout(x, m(u));
  }
  function w(u) {
    return l = void 0, _ && s ? f(u) : (s = i = void 0, r);
  }
  function C() {
    l !== void 0 && clearTimeout(l), h = 0, s = d = i = l = void 0;
  }
  function a() {
    return l === void 0 ? r : w(F());
  }
  function y() {
    var u = F(), E = p(u);
    if (s = arguments, i = this, d = u, E) {
      if (l === void 0)
        return v(d);
      if (c)
        return clearTimeout(l), l = setTimeout(x, t), f(d);
    }
    return l === void 0 && (l = setTimeout(x, t)), r;
  }
  return y.cancel = C, y.flush = a, y;
}
var ie = {
  exports: {}
}, A = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var je = T, Ne = Symbol.for("react.element"), Ae = Symbol.for("react.fragment"), Fe = Object.prototype.hasOwnProperty, ze = je.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, We = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function le(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) Fe.call(t, s) && !We.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Ne,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: ze.current
  };
}
A.Fragment = Ae;
A.jsx = le;
A.jsxs = le;
ie.exports = A;
var b = ie.exports;
const {
  SvelteComponent: qe,
  assign: Z,
  binding_callbacks: Q,
  check_outros: Me,
  children: ce,
  claim_element: ae,
  claim_space: De,
  component_subscribe: $,
  compute_slots: Be,
  create_slot: Ue,
  detach: P,
  element: ue,
  empty: ee,
  exclude_internal_props: te,
  get_all_dirty_from_scope: Ge,
  get_slot_changes: He,
  group_outros: Ke,
  init: Ve,
  insert_hydration: j,
  safe_not_equal: Je,
  set_custom_element_data: de,
  space: Xe,
  transition_in: N,
  transition_out: G,
  update_slot_base: Ye
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ze,
  getContext: Qe,
  onDestroy: $e,
  setContext: et
} = window.__gradio__svelte__internal;
function ne(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Ue(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = ue("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = ae(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ce(t);
      i && i.l(r), r.forEach(P), this.h();
    },
    h() {
      de(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      j(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && Ye(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? He(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ge(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (N(i, n), o = !0);
    },
    o(n) {
      G(i, n), o = !1;
    },
    d(n) {
      n && P(t), i && i.d(n), e[9](null);
    }
  };
}
function tt(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && ne(e)
  );
  return {
    c() {
      t = ue("react-portal-target"), o = Xe(), n && n.c(), s = ee(), this.h();
    },
    l(r) {
      t = ae(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ce(t).forEach(P), o = De(r), n && n.l(r), s = ee(), this.h();
    },
    h() {
      de(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      j(r, t, l), e[8](t), j(r, o, l), n && n.m(r, l), j(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && N(n, 1)) : (n = ne(r), n.c(), N(n, 1), n.m(s.parentNode, s)) : n && (Ke(), G(n, 1, 1, () => {
        n = null;
      }), Me());
    },
    i(r) {
      i || (N(n), i = !0);
    },
    o(r) {
      G(n), i = !1;
    },
    d(r) {
      r && (P(t), P(o), P(s)), e[8](null), n && n.d(r);
    }
  };
}
function re(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function nt(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Be(n);
  let {
    svelteInit: d
  } = t;
  const h = S(re(t)), g = S();
  $(e, g, (a) => o(0, s = a));
  const c = S();
  $(e, c, (a) => o(1, i = a));
  const _ = [], f = Qe("$$ms-gr-react-wrapper"), {
    slotKey: v,
    slotIndex: m,
    subSlotIndex: p
  } = he() || {}, x = d({
    parent: f,
    props: h,
    target: g,
    slot: c,
    slotKey: v,
    slotIndex: m,
    subSlotIndex: p,
    onDestroy(a) {
      _.push(a);
    }
  });
  et("$$ms-gr-react-wrapper", x), Ze(() => {
    h.set(re(t));
  }), $e(() => {
    _.forEach((a) => a());
  });
  function w(a) {
    Q[a ? "unshift" : "push"](() => {
      s = a, g.set(s);
    });
  }
  function C(a) {
    Q[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    o(17, t = Z(Z({}, t), te(a))), "svelteInit" in a && o(5, d = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = te(t), [s, i, g, c, l, d, r, n, w, C];
}
class rt extends qe {
  constructor(t) {
    super(), Ve(this, t, nt, tt, Je, {
      svelteInit: 5
    });
  }
}
const oe = window.ms_globals.rerender, z = window.ms_globals.tree;
function ot(e, t = {}) {
  function o(s) {
    const i = S(), n = new rt({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, d = r.parent ?? z;
          return d.nodes = [...d.nodes, l], oe({
            createPortal: B,
            node: z
          }), r.onDestroy(() => {
            d.nodes = d.nodes.filter((h) => h.svelteInstance !== i), oe({
              createPortal: B,
              node: z
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const st = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function it(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = lt(o, s), t;
  }, {}) : {};
}
function lt(e, t) {
  return typeof t == "number" && !st.includes(e) ? t + "px" : t;
}
function H(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = T.Children.toArray(e._reactElement.props.children).map((n) => {
      if (T.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = H(n.props.el);
        return T.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...T.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(B(T.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: d
    }) => {
      o.addEventListener(l, r, d);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = H(n);
      t.push(...l), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function ct(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const at = fe(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = K(), [l, d] = R([]), {
    forceClone: h
  } = ge(), g = h ? !0 : t;
  return O(() => {
    var v;
    if (!r.current || !e)
      return;
    let c = e;
    function _() {
      let m = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (m = c.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), ct(n, m), o && m.classList.add(...o.split(" ")), s) {
        const p = it(s);
        Object.keys(p).forEach((x) => {
          m.style[x] = p[x];
        });
      }
    }
    let f = null;
    if (g && window.MutationObserver) {
      let m = function() {
        var C, a, y;
        (C = r.current) != null && C.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: x,
          clonedElement: w
        } = H(e);
        c = w, d(x), c.style.display = "contents", _(), (y = r.current) == null || y.appendChild(c);
      };
      m();
      const p = Se(() => {
        m(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      f = new window.MutationObserver(p), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", _(), (v = r.current) == null || v.appendChild(c);
    return () => {
      var m, p;
      c.style.display = "", (m = r.current) != null && m.contains(c) && ((p = r.current) == null || p.removeChild(c)), f == null || f.disconnect();
    };
  }, [e, g, o, s, n, i]), T.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function se(e, t) {
  return e ? /* @__PURE__ */ b.jsx(at, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function W({
  key: e,
  slots: t,
  targets: o
}, s) {
  return t[e] ? (...i) => o ? o.map((n, r) => /* @__PURE__ */ b.jsx(J, {
    params: i,
    forceClone: !0,
    children: se(n, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ b.jsx(J, {
    params: i,
    forceClone: !0,
    children: se(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
function q(e) {
  const t = K(e);
  return t.current = e, me((...o) => {
    var s;
    return (s = t.current) == null ? void 0 : s.call(t, ...o);
  }, []);
}
function ut(e) {
  const [t, o] = R((e == null ? void 0 : e.eta) ?? null), {
    status: s,
    progress: i,
    queue_position: n,
    message: r,
    queue_size: l
  } = e || {}, [d, h] = R(0), [g, c] = R(0), [_, f] = R(null), [v, m] = R(null), [p, x] = R(null), w = K(!1), C = q(() => {
    requestAnimationFrame(() => {
      c((performance.now() - d) / 1e3), w.current && C();
    });
  }), a = q(() => {
    o(null), f(null), m(null), h(performance.now()), c(0), w.current = !0, C();
  }), y = q(() => {
    c(0), o(null), f(null), m(null), w.current = !1;
  });
  return O(() => {
    s === "pending" ? a() : y();
  }, [a, s, y]), O(() => {
    o((e == null ? void 0 : e.eta) ?? null);
  }, [e == null ? void 0 : e.eta]), O(() => {
    let u = t;
    u === null && (u = _, o(u)), u !== null && _ !== u && (m(((performance.now() - d) / 1e3 + u).toFixed(1)), f(u));
  }, [t, _, d]), O(() => {
    x(g.toFixed(1));
  }, [g]), O(() => () => {
    w.current && y();
  }, []), {
    eta: t,
    formattedEta: v,
    formattedTimer: p,
    progress: i,
    queuePosition: n,
    queueSize: l,
    status: s,
    message: r
  };
}
let M = null;
function D(e) {
  const t = ["", "k", "M", "G", "T", "P", "E", "Z"];
  let o = 0;
  for (; e > 1e3 && o < t.length - 1; )
    e /= 1e3, o++;
  const s = t[o];
  return (Number.isInteger(e) ? e : e.toFixed(1)) + s;
}
const ft = ot(({
  slots: e,
  children: t,
  configType: o,
  loadingStatus: s,
  className: i,
  id: n,
  style: r,
  setSlotParams: l,
  showMask: d,
  showTimer: h,
  loadingText: g
}) => {
  var I, L, V;
  let c = null, _ = null;
  const {
    status: f,
    message: v,
    progress: m,
    queuePosition: p,
    queueSize: x,
    eta: w,
    formattedEta: C,
    formattedTimer: a
  } = ut(s), y = f === "pending" || f === "generating", u = e.loadingText || typeof g == "string", {
    token: E
  } = xe.useToken();
  if (y)
    if (e.render)
      c = (I = W({
        setSlotParams: l,
        slots: e,
        key: "render"
      })) == null ? void 0 : I(s);
    else
      switch (o) {
        case "antd":
          c = /* @__PURE__ */ b.jsx(we, {
            size: "small",
            delay: 200,
            style: {
              zIndex: E.zIndexPopupBase,
              backgroundColor: d ? E.colorBgMask : void 0
            },
            tip: u ? e.loadingText ? (L = W({
              setSlotParams: l,
              slots: e,
              key: "loadingText"
            })) == null ? void 0 : L(s) : g : f === "pending" ? /* @__PURE__ */ b.jsxs("div", {
              style: {
                textShadow: "none"
              },
              children: [m ? m.map((k) => /* @__PURE__ */ b.jsx(T.Fragment, {
                children: k.index != null && /* @__PURE__ */ b.jsxs(b.Fragment, {
                  children: [k.length != null ? `${D(k.index || 0)}/${D(k.length)}` : `${D(k.index || 0)}`, k.unit, " "]
                })
              }, k.index)) : p !== null && x !== void 0 && typeof p == "number" && p >= 0 ? `queue: ${p + 1}/${x} |` : p === 0 ? "processing |" : null, " ", h && /* @__PURE__ */ b.jsxs(b.Fragment, {
                children: [a, w ? `/${C}` : "", "s"]
              })]
            }) : null,
            className: "ms-gr-auto-loading-default-antd",
            children: /* @__PURE__ */ b.jsx("div", {})
          });
          break;
      }
  if (f === "error" && !M)
    if (e.errorRender)
      _ = (V = W({
        setSlotParams: l,
        slots: e,
        key: "errorRender"
      })) == null ? void 0 : V(s);
    else
      switch (o) {
        case "antd":
          M = _ = /* @__PURE__ */ b.jsx(be, {
            closable: !0,
            className: "ms-gr-auto-loading-error-default-antd",
            style: {
              zIndex: E.zIndexPopupBase
            },
            message: "Error",
            description: v,
            type: "error",
            onClose: () => {
              M = null;
            }
          });
          break;
      }
  return /* @__PURE__ */ b.jsxs("div", {
    className: i,
    id: n,
    style: r,
    children: [c, _, t]
  });
});
export {
  ft as AutoLoading,
  ft as default
};
