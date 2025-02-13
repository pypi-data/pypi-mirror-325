import { i as we, a as H, r as Ce, b as be, g as ye, w as F, c as Ie } from "./Index-Dnpksb3-.js";
const k = window.ms_globals.React, xe = window.ms_globals.React.forwardRef, V = window.ms_globals.React.useRef, le = window.ms_globals.React.useState, U = window.ms_globals.React.useEffect, se = window.ms_globals.React.useMemo, B = window.ms_globals.ReactDOM.createPortal, Ee = window.ms_globals.internalContext.useContextPropsContext, N = window.ms_globals.internalContext.ContextPropsProvider, ve = window.ms_globals.antd.Cascader, Re = window.ms_globals.createItemsContext.createItemsContext;
var Se = /\s/;
function ke(e) {
  for (var n = e.length; n-- && Se.test(e.charAt(n)); )
    ;
  return n;
}
var je = /^\s+/;
function Oe(e) {
  return e && e.slice(0, ke(e) + 1).replace(je, "");
}
var X = NaN, Te = /^[-+]0x[0-9a-f]+$/i, Fe = /^0b[01]+$/i, Pe = /^0o[0-7]+$/i, Le = parseInt;
function Y(e) {
  if (typeof e == "number")
    return e;
  if (we(e))
    return X;
  if (H(e)) {
    var n = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = H(n) ? n + "" : n;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = Oe(e);
  var o = Fe.test(e);
  return o || Pe.test(e) ? Le(e.slice(2), o ? 2 : 8) : Te.test(e) ? X : +e;
}
var M = function() {
  return Ce.Date.now();
}, Ne = "Expected a function", We = Math.max, Ae = Math.min;
function Me(e, n, o) {
  var s, l, t, r, i, u, x = 0, g = !1, c = !1, _ = !0;
  if (typeof e != "function")
    throw new TypeError(Ne);
  n = Y(n) || 0, H(o) && (g = !!o.leading, c = "maxWait" in o, t = c ? We(Y(o.maxWait) || 0, n) : t, _ = "trailing" in o ? !!o.trailing : _);
  function d(h) {
    var C = s, S = l;
    return s = l = void 0, x = h, r = e.apply(S, C), r;
  }
  function b(h) {
    return x = h, i = setTimeout(p, n), g ? d(h) : r;
  }
  function a(h) {
    var C = h - u, S = h - x, T = n - C;
    return c ? Ae(T, t - S) : T;
  }
  function m(h) {
    var C = h - u, S = h - x;
    return u === void 0 || C >= n || C < 0 || c && S >= t;
  }
  function p() {
    var h = M();
    if (m(h))
      return y(h);
    i = setTimeout(p, a(h));
  }
  function y(h) {
    return i = void 0, _ && s ? d(h) : (s = l = void 0, r);
  }
  function v() {
    i !== void 0 && clearTimeout(i), x = 0, s = u = l = i = void 0;
  }
  function f() {
    return i === void 0 ? r : y(M());
  }
  function R() {
    var h = M(), C = m(h);
    if (s = arguments, l = this, u = h, C) {
      if (i === void 0)
        return b(u);
      if (c)
        return clearTimeout(i), i = setTimeout(p, n), d(u);
    }
    return i === void 0 && (i = setTimeout(p, n)), r;
  }
  return R.cancel = v, R.flush = f, R;
}
function De(e, n) {
  return be(e, n);
}
var ie = {
  exports: {}
}, W = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Ve = k, Ue = Symbol.for("react.element"), Be = Symbol.for("react.fragment"), He = Object.prototype.hasOwnProperty, qe = Ve.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, ze = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ce(e, n, o) {
  var s, l = {}, t = null, r = null;
  o !== void 0 && (t = "" + o), n.key !== void 0 && (t = "" + n.key), n.ref !== void 0 && (r = n.ref);
  for (s in n) He.call(n, s) && !ze.hasOwnProperty(s) && (l[s] = n[s]);
  if (e && e.defaultProps) for (s in n = e.defaultProps, n) l[s] === void 0 && (l[s] = n[s]);
  return {
    $$typeof: Ue,
    type: e,
    key: t,
    ref: r,
    props: l,
    _owner: qe.current
  };
}
W.Fragment = Be;
W.jsx = ce;
W.jsxs = ce;
ie.exports = W;
var w = ie.exports;
const {
  SvelteComponent: Ge,
  assign: K,
  binding_callbacks: Q,
  check_outros: Je,
  children: ae,
  claim_element: ue,
  claim_space: Xe,
  component_subscribe: Z,
  compute_slots: Ye,
  create_slot: Ke,
  detach: j,
  element: de,
  empty: $,
  exclude_internal_props: ee,
  get_all_dirty_from_scope: Qe,
  get_slot_changes: Ze,
  group_outros: $e,
  init: en,
  insert_hydration: P,
  safe_not_equal: nn,
  set_custom_element_data: fe,
  space: tn,
  transition_in: L,
  transition_out: q,
  update_slot_base: rn
} = window.__gradio__svelte__internal, {
  beforeUpdate: on,
  getContext: ln,
  onDestroy: sn,
  setContext: cn
} = window.__gradio__svelte__internal;
function ne(e) {
  let n, o;
  const s = (
    /*#slots*/
    e[7].default
  ), l = Ke(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      n = de("svelte-slot"), l && l.c(), this.h();
    },
    l(t) {
      n = ue(t, "SVELTE-SLOT", {
        class: !0
      });
      var r = ae(n);
      l && l.l(r), r.forEach(j), this.h();
    },
    h() {
      fe(n, "class", "svelte-1rt0kpf");
    },
    m(t, r) {
      P(t, n, r), l && l.m(n, null), e[9](n), o = !0;
    },
    p(t, r) {
      l && l.p && (!o || r & /*$$scope*/
      64) && rn(
        l,
        s,
        t,
        /*$$scope*/
        t[6],
        o ? Ze(
          s,
          /*$$scope*/
          t[6],
          r,
          null
        ) : Qe(
          /*$$scope*/
          t[6]
        ),
        null
      );
    },
    i(t) {
      o || (L(l, t), o = !0);
    },
    o(t) {
      q(l, t), o = !1;
    },
    d(t) {
      t && j(n), l && l.d(t), e[9](null);
    }
  };
}
function an(e) {
  let n, o, s, l, t = (
    /*$$slots*/
    e[4].default && ne(e)
  );
  return {
    c() {
      n = de("react-portal-target"), o = tn(), t && t.c(), s = $(), this.h();
    },
    l(r) {
      n = ue(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ae(n).forEach(j), o = Xe(r), t && t.l(r), s = $(), this.h();
    },
    h() {
      fe(n, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      P(r, n, i), e[8](n), P(r, o, i), t && t.m(r, i), P(r, s, i), l = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? t ? (t.p(r, i), i & /*$$slots*/
      16 && L(t, 1)) : (t = ne(r), t.c(), L(t, 1), t.m(s.parentNode, s)) : t && ($e(), q(t, 1, 1, () => {
        t = null;
      }), Je());
    },
    i(r) {
      l || (L(t), l = !0);
    },
    o(r) {
      q(t), l = !1;
    },
    d(r) {
      r && (j(n), j(o), j(s)), e[8](null), t && t.d(r);
    }
  };
}
function te(e) {
  const {
    svelteInit: n,
    ...o
  } = e;
  return o;
}
function un(e, n, o) {
  let s, l, {
    $$slots: t = {},
    $$scope: r
  } = n;
  const i = Ye(t);
  let {
    svelteInit: u
  } = n;
  const x = F(te(n)), g = F();
  Z(e, g, (f) => o(0, s = f));
  const c = F();
  Z(e, c, (f) => o(1, l = f));
  const _ = [], d = ln("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: a,
    subSlotIndex: m
  } = ye() || {}, p = u({
    parent: d,
    props: x,
    target: g,
    slot: c,
    slotKey: b,
    slotIndex: a,
    subSlotIndex: m,
    onDestroy(f) {
      _.push(f);
    }
  });
  cn("$$ms-gr-react-wrapper", p), on(() => {
    x.set(te(n));
  }), sn(() => {
    _.forEach((f) => f());
  });
  function y(f) {
    Q[f ? "unshift" : "push"](() => {
      s = f, g.set(s);
    });
  }
  function v(f) {
    Q[f ? "unshift" : "push"](() => {
      l = f, c.set(l);
    });
  }
  return e.$$set = (f) => {
    o(17, n = K(K({}, n), ee(f))), "svelteInit" in f && o(5, u = f.svelteInit), "$$scope" in f && o(6, r = f.$$scope);
  }, n = ee(n), [s, l, g, c, i, u, r, t, y, v];
}
class dn extends Ge {
  constructor(n) {
    super(), en(this, n, un, an, nn, {
      svelteInit: 5
    });
  }
}
const re = window.ms_globals.rerender, D = window.ms_globals.tree;
function fn(e, n = {}) {
  function o(s) {
    const l = F(), t = new dn({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: l,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: n.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? D;
          return u.nodes = [...u.nodes, i], re({
            createPortal: B,
            node: D
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((x) => x.svelteInstance !== l), re({
              createPortal: B,
              node: D
            });
          }), i;
        },
        ...s.props
      }
    });
    return l.set(t), t;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const mn = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function hn(e) {
  return e ? Object.keys(e).reduce((n, o) => {
    const s = e[o];
    return n[o] = pn(o, s), n;
  }, {}) : {};
}
function pn(e, n) {
  return typeof n == "number" && !mn.includes(e) ? n + "px" : n;
}
function z(e) {
  const n = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const l = k.Children.toArray(e._reactElement.props.children).map((t) => {
      if (k.isValidElement(t) && t.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = z(t.props.el);
        return k.cloneElement(t, {
          ...t.props,
          el: i,
          children: [...k.Children.toArray(t.props.children), ...r]
        });
      }
      return null;
    });
    return l.originalChildren = e._reactElement.props.children, n.push(B(k.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: l
    }), o)), {
      clonedElement: o,
      portals: n
    };
  }
  Object.keys(e.getEventListeners()).forEach((l) => {
    e.getEventListeners(l).forEach(({
      listener: r,
      type: i,
      useCapture: u
    }) => {
      o.addEventListener(i, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let l = 0; l < s.length; l++) {
    const t = s[l];
    if (t.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = z(t);
      n.push(...i), o.appendChild(r);
    } else t.nodeType === 3 && o.appendChild(t.cloneNode());
  }
  return {
    clonedElement: o,
    portals: n
  };
}
function _n(e, n) {
  e && (typeof e == "function" ? e(n) : e.current = n);
}
const E = xe(({
  slot: e,
  clone: n,
  className: o,
  style: s,
  observeAttributes: l
}, t) => {
  const r = V(), [i, u] = le([]), {
    forceClone: x
  } = Ee(), g = x ? !0 : n;
  return U(() => {
    var b;
    if (!r.current || !e)
      return;
    let c = e;
    function _() {
      let a = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (a = c.children[0], a.tagName.toLowerCase() === "react-portal-target" && a.children[0] && (a = a.children[0])), _n(t, a), o && a.classList.add(...o.split(" ")), s) {
        const m = hn(s);
        Object.keys(m).forEach((p) => {
          a.style[p] = m[p];
        });
      }
    }
    let d = null;
    if (g && window.MutationObserver) {
      let a = function() {
        var v, f, R;
        (v = r.current) != null && v.contains(c) && ((f = r.current) == null || f.removeChild(c));
        const {
          portals: p,
          clonedElement: y
        } = z(e);
        c = y, u(p), c.style.display = "contents", _(), (R = r.current) == null || R.appendChild(c);
      };
      a();
      const m = Me(() => {
        a(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: l
        });
      }, 50);
      d = new window.MutationObserver(m), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", _(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var a, m;
      c.style.display = "", (a = r.current) != null && a.contains(c) && ((m = r.current) == null || m.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, g, o, s, t, l]), k.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function gn(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function xn(e, n = !1) {
  try {
    if (Ie(e))
      return e;
    if (n && !gn(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function I(e, n) {
  return se(() => xn(e, n), [e, n]);
}
function wn({
  value: e,
  onValueChange: n
}) {
  const [o, s] = le(e), l = V(n);
  l.current = n;
  const t = V(o);
  return t.current = o, U(() => {
    l.current(o);
  }, [o]), U(() => {
    De(e, t.current) || s(e);
  }, [e]), [o, s];
}
function me(e, n, o) {
  const s = e.filter(Boolean);
  if (s.length !== 0)
    return s.map((l, t) => {
      var x;
      if (typeof l != "object")
        return n != null && n.fallback ? n.fallback(l) : l;
      const r = {
        ...l.props,
        key: ((x = l.props) == null ? void 0 : x.key) ?? (o ? `${o}-${t}` : `${t}`)
      };
      let i = r;
      Object.keys(l.slots).forEach((g) => {
        if (!l.slots[g] || !(l.slots[g] instanceof Element) && !l.slots[g].el)
          return;
        const c = g.split(".");
        c.forEach((p, y) => {
          i[p] || (i[p] = {}), y !== c.length - 1 && (i = r[p]);
        });
        const _ = l.slots[g];
        let d, b, a = (n == null ? void 0 : n.clone) ?? !1, m = n == null ? void 0 : n.forceClone;
        _ instanceof Element ? d = _ : (d = _.el, b = _.callback, a = _.clone ?? a, m = _.forceClone ?? m), m = m ?? !!b, i[c[c.length - 1]] = d ? b ? (...p) => (b(c[c.length - 1], p), /* @__PURE__ */ w.jsx(N, {
          params: p,
          forceClone: m,
          children: /* @__PURE__ */ w.jsx(E, {
            slot: d,
            clone: a
          })
        })) : /* @__PURE__ */ w.jsx(N, {
          forceClone: m,
          children: /* @__PURE__ */ w.jsx(E, {
            slot: d,
            clone: a
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const u = (n == null ? void 0 : n.children) || "children";
      return l[u] ? r[u] = me(l[u], n, `${t}`) : n != null && n.children && (r[u] = void 0, Reflect.deleteProperty(r, u)), r;
    });
}
function oe(e, n) {
  return e ? /* @__PURE__ */ w.jsx(E, {
    slot: e,
    clone: n == null ? void 0 : n.clone
  }) : null;
}
function O({
  key: e,
  slots: n,
  targets: o
}, s) {
  return n[e] ? (...l) => o ? o.map((t, r) => /* @__PURE__ */ w.jsx(N, {
    params: l,
    forceClone: !0,
    children: oe(t, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ w.jsx(N, {
    params: l,
    forceClone: !0,
    children: oe(n[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const {
  useItems: Cn,
  withItemsContextProvider: bn,
  ItemHandler: En
} = Re("antd-cascader-options");
function yn(e) {
  return typeof e == "object" && e !== null ? e : {};
}
const vn = fn(bn(["default", "options"], ({
  slots: e,
  children: n,
  onValueChange: o,
  onChange: s,
  displayRender: l,
  elRef: t,
  getPopupContainer: r,
  tagRender: i,
  maxTagPlaceholder: u,
  dropdownRender: x,
  optionRender: g,
  showSearch: c,
  options: _,
  setSlotParams: d,
  onLoadData: b,
  ...a
}) => {
  const m = I(r), p = I(l), y = I(i), v = I(g), f = I(x), R = I(u), h = typeof c == "object" || e["showSearch.render"], C = yn(c), S = I(C.filter), T = I(C.render), he = I(C.sort), [pe, _e] = wn({
    onValueChange: o,
    value: a.value
  }), {
    items: A
  } = Cn(), G = A.options.length > 0 ? A.options : A.default;
  return /* @__PURE__ */ w.jsxs(w.Fragment, {
    children: [/* @__PURE__ */ w.jsx("div", {
      style: {
        display: "none"
      },
      children: n
    }), /* @__PURE__ */ w.jsx(ve, {
      ...a,
      ref: t,
      value: pe,
      options: se(() => _ || me(G, {
        clone: !0
      }), [_, G]),
      showSearch: h ? {
        ...C,
        filter: S || C.filter,
        render: e["showSearch.render"] ? O({
          slots: e,
          setSlotParams: d,
          key: "showSearch.render"
        }) : T || C.render,
        sort: he || C.sort
      } : c,
      loadData: b,
      optionRender: v,
      getPopupContainer: m,
      prefix: e.prefix ? /* @__PURE__ */ w.jsx(E, {
        slot: e.prefix
      }) : a.prefix,
      dropdownRender: e.dropdownRender ? O({
        slots: e,
        setSlotParams: d,
        key: "dropdownRender"
      }) : f,
      displayRender: e.displayRender ? O({
        slots: e,
        setSlotParams: d,
        key: "displayRender"
      }) : p,
      tagRender: e.tagRender ? O({
        slots: e,
        setSlotParams: d,
        key: "tagRender"
      }) : y,
      onChange: (J, ...ge) => {
        s == null || s(J, ...ge), _e(J);
      },
      suffixIcon: e.suffixIcon ? /* @__PURE__ */ w.jsx(E, {
        slot: e.suffixIcon
      }) : a.suffixIcon,
      expandIcon: e.expandIcon ? /* @__PURE__ */ w.jsx(E, {
        slot: e.expandIcon
      }) : a.expandIcon,
      removeIcon: e.removeIcon ? /* @__PURE__ */ w.jsx(E, {
        slot: e.removeIcon
      }) : a.removeIcon,
      notFoundContent: e.notFoundContent ? /* @__PURE__ */ w.jsx(E, {
        slot: e.notFoundContent
      }) : a.notFoundContent,
      maxTagPlaceholder: e.maxTagPlaceholder ? O({
        slots: e,
        setSlotParams: d,
        key: "maxTagPlaceholder"
      }) : R || u,
      allowClear: e["allowClear.clearIcon"] ? {
        clearIcon: /* @__PURE__ */ w.jsx(E, {
          slot: e["allowClear.clearIcon"]
        })
      } : a.allowClear
    })]
  });
}));
export {
  vn as Cascader,
  vn as default
};
